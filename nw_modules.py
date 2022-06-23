#/usr/bin/python3.8
#modules for running different az network commands

from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient


# Acquire a credential object
credential = DefaultAzureCredential()


def get_subs():
    sub_client = SubscriptionClient(credential)
    sub_group = sub_client.subscriptions.list()
    sub_list = []
    for group in sub_group:
        sub_list.append(group.subscription_id)
    return sub_list


def get_lb(sub_list2):
    lb_list = []
    res_gr_list = []
    for sub in sub_list2:
        res_client = ResourceManagementClient(credential, sub)
        for item in res_client.resource_groups.list():
            res_gr_list.append(item.name)
    print(res_gr_list)

def get_lb_sub(sub_list2):
    lb_list = []
    for sub in sub_list2:
        net_client = NetworkManagementClient(credential, sub)
        lb = net_client.load_balancers
        print(lb.type)

def main():
    if __name__ == "__main__":
        test_list = get_subs()
        #get_lb(test_list)
        get_lb_sub(test_list)

main()
