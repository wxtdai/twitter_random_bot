
def add_header_text(choiced_text: str):
    header = "ランダムに選ばれた{}はこれです！\n".format("数字" if choiced_text.isdecimal() else "行")
    ret = header + choiced_text
    if(len(ret)>140):
        ret = ret[:137] + "..."
    assert(len(ret)<=140)
    return ret

