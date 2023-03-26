# k8s-config-generator
## Overview
`k8s-config-generator` is a Python script that generates Kubernetes configuration files for a specified number of teams. The generated files include namespaces, roles, role bindings, quotas, and client certificates. The script takes command-line arguments to configure the generated files.

## Installation
1. Clone this repository to your local machine:
``` bash 
git clone https://github.com/your_username/k8s-config-generator.git
```
2. Install the required packages:
``` bash
pip install -r requirements.txt
```

## Usage
To use `k8s-config-generator`, run the following command:

``` bash
python k8s_config.py --out_directory <output_directory> --namespace_count <number_of_namespaces> --kubeconfig_path <path_to_kubeconfig> --cpu_limit <cpu_limit> --memory_limit <memory_limit> --cpu_request <cpu_request> --memory_request <memory_request> --role_resources <role_resources> --verbs <verbs>
```

The command-line arguments are as follows:

- `--out_directory`: The directory where the generated files will be saved.
- `--namespace_count`: The number of namespaces to generate.
- `--kubeconfig_path`: The path to the kubeconfig file.
- `--cpu_limit`: The CPU limit for the quota.
- `--memory_limit`: The memory limit for the quota.
- `--cpu_request`: The CPU request for the quota.
- `--memory_request`: The memory request for the quota.
- `--role_resources`: The resources that the role will have access to.
- `--verbs`: The verbs that the role will have access to.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
