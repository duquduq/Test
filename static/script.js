function toggleContent() {
    const content = document.getElementById("hiddenContent");
    if (content.style.display === "none") {
        content.style.display = "block";
    } else {
        content.style.display = "none";
    }
}

//챔피언 검색 칸
function filterChampions() {
    const searchInput = document.getElementById("championSearch").value.toLowerCase();
    const tableRows = document.querySelectorAll(".champion-table tbody tr");
    
    tableRows.forEach(row => {
        const championName = row.querySelector(".champion-info span").textContent.toLowerCase();
        if (championName.includes(searchInput)) {
            row.style.display = ""; // 행 표시
        } else {
            row.style.display = "none"; // 행 숨기기
        }
    });
}

