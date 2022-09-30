# pip install js2py
import js2py

letter = {
  "진짜" : "인터넷에",
  "파이썬" : "이",
  "대세" : "인거 맞아?",
  "이정도만" : "하면",
  "나도" : "파이써니스타?"
}

i_am_javascript = """

function textLetter(obj) {
  console.log("develop and algorthm");
  consol.log(obj);
}
"""

internet_warrior = js2py.eval_js(i_am_javascript)

print(internet_warrior(letter))