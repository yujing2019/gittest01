
import  pymysql
def conn():
    return pymysql.connect(host ="127.0.0.1",user="root",password="12345678",db='stu')





def l_f_mysql(fname):
    conn1=conn()
    try:
        with open(fname) as fin:
            for lin in fin:
                if len(lin)>0:
                    lin=lin.strip()
                    sid,chinese,english,math=lin.split('\t')
                    sql=f"""
                        insert into sgrade (sid,chinese,english,math)
                        values('{sid}','{chinese}','{english}','{math}')
                    """
                    cursor=conn1.cursor()
                    cursor.execute(sql)
            conn1.commit()
    finally:
        if conn1 is not None:conn1.close()


def q_all_score():
    conn1 = conn()
    try:
        sql="select * from sgrade"
        cursor=conn1.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn1.close()



def q_score(sid):
    conn1 = conn()
    try:
        sql = f"""select sid,chinese,english math from sgrade where sid='{sid}'"""
        cursor = conn1.cursor()
        cursor.execute(sql)
        return cursor.fetchone()
    finally:
        conn1.close()



if __name__ == "__main__":

    #load file to mysql
    #l_f_mysql("input.txt")
    #query all scores
    sgrade=q_all_score()
    for grade in sgrade:
        print(grade)

    #query by sid
    s1=q_score("s001")
    print("grade1:",s1)
    s2=q_score("s002")
    print("grade2:",s2)


