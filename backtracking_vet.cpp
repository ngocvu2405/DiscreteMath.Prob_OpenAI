// Bài toán
// Hỏi có bao nhiêu xâu nhị phân độ dài 10 thỏa mãn điều kiện:
// Độ dài các vệt của xâu là lớn hơn hoặc bằng 2 và nhỏ hơn hoặc bằng 6
// Giữa các vệt của xâu đã cho chỉ có đúng 1 bít 0
#include<iostream>
#include<vector>
using namespace std;
int arr[100];
int count = 0;
int n; // do dai cua sau 

void print(){
    for(int i = 1; i<=n; i++){
        cout<<arr[i]<<' ';
    }
    cout<<endl;
    count++;
}

bool check(int v, int k){
    if (k == 1) return true;
    int appear_one = 0;
    if (arr[k-1] ==0 && v==0) return false;
    return true;
}

void Try(int k){
    for(int v=0; v<=1;v++){
        if(check(v,k)){
            arr[k] = v;
            if (k==n) {
                // print();
                vector<int> appear_one;
                int plus = 1;
                for(int j = 1; j<=n; j = j + plus){
                    if (arr[j]==1){
                        int count_one = 1;
                        for(int k =j+1;k<=n;k++){
                            if(arr[k]==1) {
                                plus++;
                                count_one++;
                            }
                            else break;
                        }
                        appear_one.push_back(count_one);
                    }
                    else plus = 1;
                }
                bool kkk = true;
                for(int m = 0; m<appear_one.size(); m++){
                    if (appear_one[m]>6 || appear_one[m] == 1){
                        kkk = kkk&&false;
                        break;
                    }
                }
                if (kkk == true){
                    print();
                }
            }
            else Try(k+1);
        }
    }
}

int main(){
    cin>>n;
    Try(1);
    cout<<count<<endl;
    return 0;
}