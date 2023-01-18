// Function created to update the comment
const editCommentButton = document.getElementById("edit-comment-button");
editCommentButton.addEventListener("click", unhideCommentSection);

function unhideCommentSection() {
    const commentSection = document.getElementById("hide-text-area");
    commentSection.style.display = "block";
}