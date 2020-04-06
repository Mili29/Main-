#include<bits/stdc++.h>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

signed main(){
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int i,j,x,t,count;
    cin>>t;
    count=0;
    while(t--){
        int n;
        count=count+1;
        cin>>n;
        
        std::vector<pair<pair<int,int>,int>>times,v;
        int a[n+1];
        
        for(i=0,i<n;i++;){
            int a,b;
            cin>>a>>b;
            v.push_back ({{a,1},i});
            v.push_back({{b,0},i});
            times.push_back ({{a,b},i});
        }
        
        int num=0;
        sort(v.begin(),v.end());
        unordered_map<int,int>m;
        for(int i=0;i<v.size();i++){
            x=v[i].first.first;
            
            if(m[x]==0){
                num++;
                m[x]=num;
            }
        }
        set<int> st;
        st.insert(1);
        st.insert(2);
        bool okay=true;
        int d=0;
        for(i=0;i<v.size();i++){
            if(v[i].first.second==0){
                d--;
                st.insert(a[v[i].second]);
            }
            else{
                d++;
                if(d>2){
                    okay=false;
                    break;
                }
                auto it=st.begin();
                a[v[i].second]=*it;
                st.erase(it);
                
            }
        }
        
        cout<<"Case #"<<count<<": ";
        if(!okay)
            cout<<"IMPOSSIBLE"<<endl;
        else{
            for(int i=0;i<n;i++){
                if(a[i]==1){
                    cout<<"C";
                }
                else{
                    cout<<"J";
                }
            }
            cout<<endl;
        }
        
    }
}
