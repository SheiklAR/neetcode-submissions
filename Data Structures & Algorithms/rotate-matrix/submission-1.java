class Solution {
    public void rotate(int[][] matrix) {

        int ROWS = matrix.length;
        int COLS = matrix[0].length;

        // Transpose
        for (int i = 0; i < ROWS; i++ ) {
            for (int j = i+1; j < COLS; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Reverse
        // System.out.println(Arrays.toString(matrix[0]));

        for (int i = 0; i < ROWS; i++) {
            reverseRow(matrix, i, COLS);
        }
        
    }

     private void reverseRow(int[][] arr, int row, int COLS) {
        System.out.println("here");
        int l = 0; 
        int r = COLS - 1;
        while (l < r) {
            int temp = arr[row][l];
            arr[row][l] = arr[row][r];
            arr[row][r] = temp;
            l++; r--;
        }
        }
}
