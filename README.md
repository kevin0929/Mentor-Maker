# 導師挑選器

### 注意事項
1. 請務必將 ```main.py``` 與 ```tkfile.py``` 放在同一個資料夾底下。
2. ```member.csv``` 僅供參考。

### 挑選介面

![image](https://user-images.githubusercontent.com/37032234/172646555-fce5597b-10a5-425e-b213-4c164efc2d95.png)

1. 點擊匯入檔案，挑選欲匯入之 ```csv``` 檔。
2. 在下拉式選單中選擇 ```要挑選的導師數目```, ```第一順位```, ```第二順位```。
3. 點選匯入資訊，觸發運算事件。
4. 點選確認。

### 結果介面

![image](https://user-images.githubusercontent.com/37032234/172647832-c3af2509-7427-4daf-a8e2-f7ec90a6c705.png)

1. 假設欲選擇 $6$ 位導師。
2. 第一順位是 **當過的年份**。
3. 第二順位是 **有沒有意願**。

### 判斷之策略

1. 第一順位: 當過的年份，第二順位: 有沒有意願

![image](https://user-images.githubusercontent.com/37032234/172648392-7f40322a-c4f9-42fd-9d53-0eaf8ccb7d77.png)

2. 第一順位: 有沒有意願，第二順位: 當過的年份

![image](https://user-images.githubusercontent.com/37032234/172648495-cf0cc81e-aa3a-45c7-8308-6b4ee67f4e4f.png)

