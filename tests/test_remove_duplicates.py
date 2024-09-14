import unittest
import pandas as pd
from autodatacleaner import remove_duplicates
from sklearn.datasets import load_iris
import os
import tempfile

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        # Load the Iris dataset
        iris = load_iris()
        self.iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        self.iris_df['species'] = iris.target_names[iris.target]
        
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.test_dir.name, 'iris.csv')
        
        # Save the Iris dataset to a file in the temporary directory
        self.iris_df.to_csv(self.file_path, index=False)

    def test_remove_duplicates(self):
        # Introduce duplicates for testing
        self.iris_df = pd.concat([self.iris_df, self.iris_df.iloc[0:5]])  # Duplicate the first 5 rows
        self.iris_df.to_csv(self.file_path, index=False)  # Save the modified DataFrame with duplicates

        # Remove duplicates
        remove_duplicates(self.file_path)
        
        # Load the modified dataset
        df = pd.read_csv(self.file_path)
        
        # Check that the number of rows has decreased
        self.assertLess(df.shape[0], self.iris_df.shape[0])
        
        # Check that the number of unique rows is the same as the modified dataset
        self.assertEqual(df.shape[0], df.drop_duplicates().shape[0])

    def tearDown(self):
        # Clean up: Remove the temporary directory and its contents
        self.test_dir.cleanup()

if __name__ == '__main__':
    unittest.main()
