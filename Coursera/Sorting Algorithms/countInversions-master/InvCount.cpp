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

 int merge_Sort(vector<int>& numbers);
 void showVector(vector<int>& numbers);

 int main ()
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

 	invCount = merge_Sort(numbers);
 	//showVector(numbers);

 	return 0;
 }

 int merge_Sort(vector<int>& numbers)
 {
 	int mid, invCount = 0;
 	vector<int> subLeft;
 	vector<int> subRight;

 	if (numbers.size() <= 1) {
 		cout << "invCount: " << invCount << endl;
 		return invCount;
 	} else {
 		mid = (subLeft.size() + subRight.size())/2;
 		subLeft(numbers.begin(), (numbers.begin() + (mid - 1)));
 		for (vector<int>::const_iterator i = subLeft.begin(); i < subLeft.end(); ++i) {
 			cout << "subLeft contents: " << *i << ' ' << endl;
 		}
 		subRight((numbers.begin() + mid), numbers.end());
 		for (vector<int>::const_iterator i = subRight.begin(); i < subRight.end(); ++i) {
 			cout << "subRight contents: " << *i << ' ' << endl;
 		}

 		invCount = merge_Sort(subLeft);
 		invCount += merge_Sort(subRight);

 		if (subLeft.back() <= subRight.front()) {
 			subLeft.insert(subLeft.end(),subRight.begin(), subRight.end());
 		}

 		return invCount;
 		//vector<int> result = merge(subLeft, subRight);
 		//return result;
 	}
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