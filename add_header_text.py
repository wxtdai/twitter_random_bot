

def add_header_text(main_text: str):
    header = "ランダムに選ばれた{}はこれです！\n".format("数字" if main_text.isdecimal() else "行")
    ret = header + main_text
    if(len(ret)>140):
        ret = ret[:137] + "..."
    assert(len(ret)<=140)
    return ret