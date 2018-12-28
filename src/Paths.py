import os

root = os.path.realpath(
        os.path.join(
                os.path.dirname(
                        os.path.realpath(__file__)
                ),
                "../"
        )
)
raw = os.path.join(root, 'data/raw')
processed = os.path.join(root, 'data/processed')