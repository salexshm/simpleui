def sample1_on_input(hashMap,_files=None,_data=None):
    if hashMap.get("listener")=="btn_res":
        hashMap.put("toast",str(int(hashMap.get("a"))+int(hashMap.get("b"))))
    return hashMap


def sample1_on_create(hashMap,_files=None,_data=None):
    if not hashMap.containsKey("a"):
        hashMap.put("a","")
    if not hashMap.containsKey("b"):
        hashMap.put("b","")
    return hashMap
