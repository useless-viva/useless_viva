function link() {
    setTimeout(function() {
        location.href="/choices/{{user_id}}/?page={{questions.number}}";
    }, 100000);
}