from cProfile import label
from diagrams.generic.device import Tablet
from diagrams.azure.network import Firewall, DNSZones
from diagrams.azure.identity import ADB2C, ActiveDirectory
from diagrams.azure.database import CacheForRedis, DatabaseForMysqlServers
from diagrams.azure.devops import Devops, ApplicationInsights
from diagrams.azure.compute import ContainerRegistries, KubernetesServices, VMWindows
from diagrams.azure.security import KeyVaults
from diagrams.custom import Custom
from diagrams import Cluster, Diagram, Edge

with Diagram("", filename="iaas", show=False):
    client=Tablet("Client")
    public_ip = Custom("*.contoso.com", "./resources/internet.png")
    azure_request= Custom("Azure", "./resources/internet.png")
    
    with Cluster("Contoso IaaS"):
        with Cluster("Firewall VNET"):
            firewall= Firewall("Azure\nFirewall")

        with Cluster("Contoso VNET"):
            winvm=VMWindows("Jump Machine")

        with Cluster("Kubernetes VNET"):
            k8=KubernetesServices("Azure\nKubernetes\nService")
        
        with Cluster("ADDS VNET"):
            adbastion=Custom("Azure\nBastion", "./resources/bastion.png")
    
    with Cluster("Multi-tenant PaaS"):
        managed_security= Firewall("Azure\nManaged Security")
        dns=DNSZones("contoso.com")
        
        adb2c=ADB2C("Azure\nAD B2C")
        ad=ActiveDirectory("Azure\nActive Directory")
        adb2c \
            - Edge(color="orange", taillabel="federated",labeldistance="6.5", labelangle="20") \
            - ad

        with Cluster("DevSecOps"):
            devops=Devops("Azure DevOps")
            acr=ContainerRegistries("Azure\nContainer\nRegistry")
            keyvault=KeyVaults("Azure\nKey Vault")
            appinsights=ApplicationInsights("AppInsights")

        with Cluster("Managed Databases"): 
            mysql= DatabaseForMysqlServers("Azure DB\nFor MySQL")
            redis=CacheForRedis("Azure\nRedis Cache")

    purposes=[azure_request, public_ip]
    client >> purposes

    azure_request >> managed_security
    managed_security>> dns
    managed_security>> adb2c
    managed_security>>devops
    managed_security>>appinsights
    managed_security>>acr
    managed_security>>keyvault
    
    public_ip \
    >> Edge(color="black", label="Zero-Trust Connection") \
    >> firewall

    firewall >> k8
    firewall >> adbastion
    firewall >> winvm

    k8 >> mysql
    k8 >> redis
    k8 >> appinsights
    k8 >> keyvault
    k8 >> acr
    k8 << devops

    winvm >> mysql
    winvm >> redis
    winvm >> k8

    adbastion >> ad