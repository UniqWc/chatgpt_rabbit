import base
import openai


openai.api_key = base.key
# start_sequence = "\n兔宝宝:  "
start_sequence = ""
restart_sequence = "\nQ: "


def get_info(prompt):
    if prompt == "":
        return "请输入您好奇的内容"
    try:
        response = openai.Completion.create(
          model="text-davinci-003", #这里我们使用的是davinci-003的模型，准确度更高。
          prompt = prompt,
          temperature=1,
          max_tokens=2000,  #这里限制的是回答的长度，你可以可以限制字数，如:写一个300字作文等。
          frequency_penalty=0,
          presence_penalty=0
        )
        return start_sequence, response["choices"][0]["text"].strip()
    except Exception as exc: #捕获异常后打印出来
        return exc
        #return "不好意思呢，请您耐心等待，小兔刚才偷懒了"