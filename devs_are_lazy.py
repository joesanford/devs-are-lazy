from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from data_loader import get_mocked_data, get_data, languages

app = Flask(__name__)
app.debug = True
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)


@app.route('/')
def index():
    github_data = get_mocked_data()
    open_pull_requests, closed_pull_requests, pull_request_ratios, open_issues, closed_issues, issue_ratios = ([] for _ in range(6))

    for language in github_data:
        open_pull_requests.append(github_data[language]['pr']['open'])
        closed_pull_requests.append(github_data[language]['pr']['closed'])
        pull_request_ratios.append(int(github_data[language]['pr']['open'])/float(github_data[language]['pr']['closed']))
        open_issues.append(github_data[language]['issue']['open'])
        closed_issues.append(github_data[language]['issue']['closed'])
        issue_ratios.append(int(github_data[language]['issue']['open'])/float(github_data[language]['issue']['closed']))

    return render_template('index.html', open_pull_requests=open_pull_requests, closed_pull_requests=closed_pull_requests, pull_request_ratios=pull_request_ratios, open_issues=open_issues, closed_issues=closed_issues, issue_ratios=issue_ratios, labels=languages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
