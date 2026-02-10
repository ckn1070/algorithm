# 카펫

## 📌 문제 설명
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고  
테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.  

Leo는 집으로 돌아와서 아까 본 카펫의 갈색 격자 수 `brown`과  
노란색 격자 수 `yellow`는 기억했지만,  
전체 카펫의 **가로 세로 크기**는 기억하지 못했습니다.  

갈색 격자의 수와 노란색 격자의 수가 주어질 때,  
전체 카펫의 **가로 길이와 세로 길이**를 순서대로 배열에 담아 `return` 하도록  
`solution` 함수를 작성하세요. :contentReference[oaicite:0]{index=0}

---

## 📥 입력 조건
- `brown`: 갈색 격자의 수  
  - 8 이상 5,000 이하의 자연수  
- `yellow`: 노란색 격자의 수  
  - 1 이상 2,000,000 이하의 자연수  
- 카펫의 가로 길이는 세로 길이보다 크거나 같습니다. :contentReference[oaicite:1]{index=1}

---

## 📤 출력 조건
- **가로 길이, 세로 길이**를 순서대로 배열에 담아 반환합니다. :contentReference[oaicite:2]{index=2}

---

## 🔍 입출력 예시

| brown | yellow | return      |
|-------|--------|-------------|
| 10    | 2      | [4, 3]      |
| 8     | 1      | [3, 3]      |
| 24    | 24     | [8, 6]      | :contentReference[oaicite:3]{index=3}

---

## 🧠 풀이 핵심
- 전체 카펫 면적은 `brown + yellow` 입니다. :contentReference[oaicite:4]{index=4}  
- 노란색 부분은 **가로 × 세로**이고, 테두리 1줄 갈색이 둘러싸고 있으므로  
  `(가로 - 2) × (세로 - 2) = yellow`가 성립합니다. :contentReference[oaicite:5]{index=5}  
- 모든 약수 쌍을 탐색하여 조건을 만족하는 `(가로, 세로)`를 찾습니다. :contentReference[oaicite:6]{index=6}

---

## 🏷️ 분류
- 완전탐색  
- 수학  
