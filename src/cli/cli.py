import argparse

def get_input(prompt, default_value):
    value = input(f"{prompt} [default: {default_value}]: ").strip()
    return value if value else default_value

def parse_arguments():

    default_values = {
        "out_directory": "C:\\Users\\user\\Desktop\\k8s-config",
        "namespace_count": 10,
        "kubeconfig_path": "C:\\Users\\user\\.kube\\config",
        "cpu_limit": "150m",
        "memory_limit": "128Mi",
        "cpu_request": "75m",
        "memory_request": "64Mi",
        "role_resources": "deployments,pods,pods/log,pods/portforward,pods/exec,secrets,services,configmaps,events,replicasets,verbs",
        "verbs": "get,list,watch,create,update,patch,delete",
    }

    parser = argparse.ArgumentParser(description="Generate Kubernetes config files for a cluster.", add_help=False)

    parser.add_argument("-o", "--out", dest="out_directory", default=None, help="Output directory path for the generated config files.")
    parser.add_argument("-n", "--namespace", dest="namespace_count", type=int, default=None, help="Number of namespaces to create.")
    parser.add_argument("-k", "--kubeconfig", dest="kubeconfig_path", default=None, help="Path to the kubeconfig file.")
    parser.add_argument("-cl", "--cpu_limit", dest="cpu_limit", default=None, help="CPU limit quota (e.g. 500m).")
    parser.add_argument("-cr", "--cpu_request", dest="cpu_request", default=None, help="CPU request quota (e.g. 100m).")
    parser.add_argument("-ml", "--memory_limit", dest="memory_limit", default=None, help="Memory limit quota (e.g. 1Gi).")
    parser.add_argument("-mr", "--memory_request", dest="memory_request", default=None, help="Memory request quota (e.g. 128Mi).")
    parser.add_argument("-r", "--role-resources", dest="role_resources", default=None, help="Role resources in the namespace separated by commas (e.g. pods,services).")
    parser.add_argument("-v", "--verbs", dest="verbs", default=None, help="Verbs resources in the namespace separated by commas (e.g. get,list,watch).")

    parser.add_argument("--help", action="help", help="Show this help message and exit.")

    args = parser.parse_args()

    for arg_name, default_value in default_values.items():
        if getattr(args, arg_name) is None:
            setattr(args, arg_name, get_input(f"Enter {arg_name.replace('_', ' ')}", default_value))

    return args

# def main():
#     args = parse_arguments()
#     print(args)
#     # Your app logic here
#     # You can access the input values with args.out_directory, args.namespace_count, etc.

# if __name__ == "__main__":
#     main()
