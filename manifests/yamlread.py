import yaml
import sys
def replace_in_dictlist(key,key_value,dict_list,replacement):
    found = False
    for idx, item in enumerate(dict_list):
        if item[key] == key_value:
            found = True
            dict_list[idx] = replacement
    if not found:
        dict_list.append(replacement)

stream = open("kadalu-operator.yaml")
crds = list(yaml.load_all(stream))
operator={}
for crd in crds:
    if crd["metadata"]["name"] == "operator":
        operator=crd
env = operator["spec"]["template"]["spec"]["containers"][0]["env"]
kubelet_entry = {"name":"KUBELET_DIR","value":"/var/lib/kubelet"}
replace_in_dictlist("name","KUBELET_DIR",env,kubelet_entry)
print(yaml.dump_all(crds))