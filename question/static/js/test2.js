$("#answer-btn2").click(function () {
    // #result의 display가 "none"일 경우 (접혀있는 경우)
    if ($("#result_page").css("display") == "none") {
        // 감추기
        $(".num").hide();
        $(".que").hide();
        $(".box").hide();
        $(".box_ddu").hide();
        $("#page_info").hide();
        // #result_page 보이기
        $("#result_page").show();
    }
});