$("#btn2").click(function () {
    // #result의 display가 "none"일 경우 (접혀있는 경우)
    if ($("#result").css("display") == "none") {
        // #more 버튼 감추기
        $("#btn").hide();
        $("#btn2").hide();
        // #result 보이기
        $("#result").show();
    } else {
        // #result의 display가 "block"인 경우 (펼쳐져 있는 경우)
        $("#btn2").show();
    }
});