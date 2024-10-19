import json

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


def barcode_on_input(hashMap,_files=None,_data=None):
    # handlers code
    if hashMap.get("listener") == 'barcode':  # check scan event
        b = hashMap.get('barcode')  # barcode variable
        hashMap.put("toast", hashMap.get(b))
        return hashMap


def init_on_start(hashMap,_files=None,_data=None):
   hashMap.put("SQLConnectDatabase","test1.DB")
   hashMap.put("SQLExec",json.dumps(
       {
           "query":
               "create table IF NOT EXISTS Record(id integer primary key autoincrement,art text, barcode text, name text, qty real)",
           "params":
               ""
       }
   )
               )


   return hashMap