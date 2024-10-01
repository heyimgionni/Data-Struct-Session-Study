// See https://aka.ms/new-console-template for more information

int[] arr = { 87, 9, 1, 78 };
int[] sortedArr = QuickSort(arr);
Console.WriteLine(string.Join(", ", sortedArr)); // Output: 1, 9, 78, 87

static int[] QuickSort(int[] arr) {
    if(arr.Length < 2) {
        return arr;
    }
    else {
        int pivot = arr[0];
        List<int> less = new List<int>(); 
        List<int> grater = new List<int>(); 

        for (int i = 1; i < arr.Length; i++) {
            if (arr[i] < pivot) {
                less.Add(arr[i]);
            }
            if(arr[i] > pivot) {
                grater.Add(arr[i]);
            }
        }
        return 
        QuickSort(less.ToArray()).
        Concat(new int[] {pivot}).
        Concat(QuickSort(grater.ToArray())).
        ToArray();
    }
}


