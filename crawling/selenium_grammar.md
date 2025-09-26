# 1. 입력창(input Box) <input type = 'text' id = 'search_keyword'>
```
search_input = driver.find_element(By.ID, "search_keyword")
search_input.clear()
search_input.send_keys("파이썬 크롤링")
```

# 2. 버튼(Button) <button button type = 'submit'>
```
driver.find_element(By.CSS_SELECTOR, "button.btn-login")
login.click()
```

# 체크박스 <input type = 'checkbox' id = 'agree_all_terms'>
```
agree_checkbox = driver.find_element(By.ID, 'agree_all_terms')
# 현재 체크가 안 되어 있을 경우만 클릭
if not agree_checkbox.is_selected():
    agree_checkbox.click()
```

# 4. 레디오 버튼 <input type = 'radio'>
```
<input type = "radio" name = "rdoMonthPeriod" value = "period">
driver.find_element(By.CSS_SELECTOR, "input[name = 'rdoMonthPeriod] [value = 'period']")
radio.click()
```

# 5. 드랍다운 메뉴 <select id = 'year'> </select>
```
<select id = 'year'>
     <option value = "2024"> 2024년 </option>
year_dropdown = driver.find_element(By.ID, 'year')
#Select 객체로 만들어서 사용
Select(year_dropdown)
select.by_value('2024')
# select.select_by_visible_text('2024년')
```