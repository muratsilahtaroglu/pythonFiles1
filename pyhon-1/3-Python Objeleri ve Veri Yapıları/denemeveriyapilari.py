message=r"  C:\dosya1\dosya2; ;  C:\dosya1\dosya5\dosya3.tfddfxt; D:\dosya1\dosya3.c54dfs; D:\test.xm656l "
print([l[:l.find(".")] for l in [x.split("\\")[-1].strip(" ") for x in message.split(";")] if l != ""])







