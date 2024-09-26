from flask import Flask, render_template, request
from fight_simulator import group_fight

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fight', methods=['POST'])
def fight():
    # Get data from the form
    group1 = []
    group2 = []
    
    for i in range(int(request.form['group1_count'])):
        group1.append({
            'name': request.form[f'group1_name_{i}'],
            'fighting': int(request.form[f'group1_fighting_{i}']),
            'agility': int(request.form[f'group1_agility_{i}']),
            'stamina': int(request.form[f'group1_stamina_{i}']),
            'size': request.form[f'group1_size_{i}'],
            'age': request.form[f'group1_age_{i}']
        })

    for i in range(int(request.form['group2_count'])):
        group2.append({
            'name': request.form[f'group2_name_{i}'],
            'fighting': int(request.form[f'group2_fighting_{i}']),
            'agility': int(request.form[f'group2_agility_{i}']),
            'stamina': int(request.form[f'group2_stamina_{i}']),
            'size': request.form[f'group2_size_{i}'],
            'age': request.form[f'group2_age_{i}']
        })

    result = group_fight(group1, group2)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
