# render_template を追加でインポートするよ！
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 1. 裏側の計算（ここはそのまま！）
    hourly_wage = 1200
    hours_worked = 25
    current_salary = hourly_wage * hours_worked
    target_item = "ヴィンテージのデニム"
    target_price = 40000
    remaining = target_price - current_salary
    progress_percent = round((current_salary / target_price) * 100, 1)
    # 2. 画面の表示（長いHTMLの代わりに、ファイルを呼び出す！）
    # HTML側に渡したい変数を全部セットしてあげるんだ。
    return render_template('index.html', 
                           current_salary=current_salary,
                           target_item=target_item,
                           target_price=target_price,
                           remaining=remaining,
                           progress_percent = round((current_salary / target_price) * 100, 1))

@app.route('/target')
def target_page():
    # こっちもHTMLファイルを作って呼び出すだけ！
    return render_template('target.html')

if __name__ == '__main__':
    app.run(debug=True)