from src.pre_built.brazilian_jobs import read_brazilian_file

def test_brazilian_jobs():
    'return a dictionary list'
result = read_brazilian_file('test/mocks/brazilians_jobs.csv')
for job in result:
    assert 'salary' in job
    assert 'title' in job
    assert 'type' in job
