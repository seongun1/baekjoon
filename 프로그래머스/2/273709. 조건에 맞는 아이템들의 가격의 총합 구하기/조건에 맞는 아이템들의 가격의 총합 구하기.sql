-- 코드를 작성해주세요
#ITEM_ID, ITEM_NAME, RARITY, PRICE는 각각 아이템 ID, 아이템 명, 아이템의 희귀도, 아이템의 가격을 나타냅니다.
SELECT sum(price) as TOTAL_PRICE
from ITEM_INFO
where RARITY = "LEGEND"