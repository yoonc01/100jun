#include <iostream>
#include <string>

using namespace std;

int n, score, cnt;
string str;

int main(void)
{
    cin >> n;
    while(n--)
    {
        cnt = 0;
        score = 0;
        cin >> str;
        for (int i = 0; i < str.length(); i++)
        {
            if (str[i] == 'O')
            {
                cnt++;
                score = score + cnt;
            }
            else
                cnt = 0;
        }
        cout << score << '\n';
    }
}