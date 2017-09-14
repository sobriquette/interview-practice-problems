/* test file for counting inversions
 *
 * CourseEra Data Structures & Algorithms
 * by Tim Roughgarden
 *
 * Author: Melody Lin
 * Date: 01/28/2015
 */

 #include <iostream>
 #include <fstream>
 #include <vector>
 using namespace std;

 int merge_Sort(vector<int>& numbers, int left, int right);
 void showVector(vector<int>& numbers);

 int main()
 {
 	ifstream myfile;
 	myfile.open("TestArray.txt");
 	vector<int> numbers;
 	int invCount = 0;

 	if (myfile.is_open()) {
 		int currNum;
 		while (!myfile.eof()) {
 			myfile >> currNum;
 			numbers.push_back(currNum);
 		}
 	}

 	myfile.close();

 	int left = numbers.at(0);
 	cout << "left: " << left << endl;
 	int right = numbers.size();
 	cout << "right: " << right << endl;
 	invCount = merge_Sort(numbers, left, right);
 	cout << "invCount: " << invCount << endl;
 	//showVector(numbers);

 	return 0;
 }

 int merge_Sort(vector<int>& numbers, int left, int right)
 {
 	int mid = 0;
 	int countLeft = 0;
 	int countRight = 0;

 	if (left < right) {
 		mid = (left + right)/ 2;
 		cout << "mid: " << mid << endl;
 		countLeft += merge_Sort(numbers, left, mid);
 		countRight += merge_Sort(numbers, mid + 1, right);
 	}

 	return countLeft + countRight;
 }
/*
 int merge(subLeft, subRight)
 {
 	vector<int> result;
 	vector<int>::iterator i = subLeft.begin();
 	vector<int>::iterator j = subRight.begin();
 	vector<int>::iterator k = result.begin();
 	int count = 0;

 	while (i != subLeft.end() && j != subRight.end()) {
 		if (subLeft.front() <= subRight.front()) {
 			result.push_back(subLeft.front());
 			count += 1;
 			i++, k++;
 		} else {
 			result.push_back(subRight.front());
 			count += 1;
 			j++, k++;
 		}
 	}
 	
 	while (subLeft.size() > 0) {
 		result.push_back(subLeft.at(i));
 		i++, k++;
 	}

 	while (subRight.size() > 0 ) {
 		result.push_back(subRight.at(j));
 		j++, k++;
 	}
 }
*/
 void showVector(vector<int>& numbers)
 {
 	for (unsigned int i = 0; i < numbers.size(); i++) {
 		cout << "position: " << i << " ;" << "number: " << numbers.at(i) << endl;
 	}
 }