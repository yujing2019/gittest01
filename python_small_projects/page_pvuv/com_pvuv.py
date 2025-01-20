pageinfo_dict={}

with open("page_info.txt") as fin:
    for lin in fin:
        k=0
        if len(lin)>0:
            lin=lin.strip().split("\t")
            page_id,page_name=lin
            if page_id not in pageinfo_dict:
                pageinfo_dict[page_id]=page_name


"""
result={(pdate,page_id):{"pv":123 "user_id" set(),"uv":len(set)}}

"""
result={}
with open("blog_access.log") as fin1:
    for lin in fin1:
        if len(lin)>0:
            fields=lin.strip().split("\t")
            pdate,user_id,page_id,event=fields
            pdate=pdate.split(" ")[0]
            if event=="show":
                k=(pdate,page_id)
                if k not in result:
                    result[k]={}
                    result[k]["pv"]=1
                    result[k]["user"]={user_id}
                    result[k]["uv"]=len(result[k]["user"])
                else:
                    result[k]["pv"] +=1
                    result[k]["user"]=result[k]["user"] |{user_id}
                    result[k]["uv"] = len(result[k]["user"])

with open ('fout.txt','w') as fout:
    for k,v in result.items():
        pdate,page_id=k
        page_name=pageinfo_dict.get(page_id)

        output=[pdate,page_id,page_name,v["pv"],v["uv"]]
        fout.write("\t".join([str(x)for x in output])+'\n') 




