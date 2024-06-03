from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def train_lr_model(df):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    target = 'duration'
    y = df[target].values
    
    categorical = ['PULocationID', 'DOLocationID']
    train_dicts = df[categorical].to_dict(orient='records')
    dv = DictVectorizer()
    X_train = dv.fit_transform(train_dicts)

    lr = LinearRegression()
    lr.fit(X_train, y)

    print(f'Intercept: {lr.intercept_}')

    return (dv, lr, lr.intercept_)


@test
def test_output(lr, dv, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert (lr, dv) is not None, 'The output is undefined'