from kubernetes import client, config
from kubernetes.client import V1Job
import yaml


def crete_job():
    config.load_config()

    with open('job.yml') as f:
        data = yaml.safe_load(f)

    api_instance = client.BatchV1Api()
    resp = api_instance.create_namespaced_job(body=data, namespace='default')

    print('Job Created')
