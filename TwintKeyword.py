import twint

cari = input("Masukkan keyword :  ")

c = twint.Config()
c.Search = {cari}
c.Store_csv = True
c.Limit = 40
c.Custom["tweet"] = ["date","time","username","name","tweet","mentions","hashtags","likes_count"]
c.Output = "keyword.csv"

twint.run.Search(c)
