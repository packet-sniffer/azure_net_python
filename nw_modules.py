#/usr/bin/python3.8
#modules for running different az network commands

import subprocess
from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from pprint import pprint

# Acquire a credential object
credential = DefaultAzureCredential()


def get_subs():
    sub_client = SubscriptionClient(credential)#getting creds
    sub_group = sub_client.subscriptions.list()
    sub_list = []
    for group in sub_group:
        sub_list.append(group.subscription_id)
    print(sub_list)
    return sub_list


def get_lb(sub_list2):
    lb_list = []
    res_gr_list = []
    for sub in sub_list2:
        res_client = ResourceManagementClient(credential, sub)
        for item in res_client.resource_groups.list():
            res_gr_list.append(item.name)
    print(res_gr_list)

'''
def get_lb_sub(sub_list2):
    lb_list = []
    for sub in sub_list2:
        net_client = NetworkManagementClient(credential, sub)
        lb = net_client.load_balancers
        print(lb)
'''



def load_balancer_list(sub_list):
    lb_list = []
    for sub in sub_list:
        try:
            lb = subprocess.check_output(f'az network lb list --subscription {sub} --output table', stderr=subprocess.STDOUT, shell='True')
            lb = lb.decode('utf-8')
            lb = lb.split()[16]
            lb_list.append(lb)
        except:
            pass
    pprint(lb_list)


def main():
    test_list = get_subs()
    #test_list = ['39f9beb3-6ab9-4b94-9011-9a185d46e35f']
    #get_lb(test_list)
    #get_lb_sub(test_list)
    load_balancer_list(test_list)

if __name__ == "__main__"
    main()
