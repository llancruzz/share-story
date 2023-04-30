// Function created to update the comment

function unhideCommentSection(event) {
  const editButton = event.target;
  const commentSection = editButton.previousElementSibling;
  // const commentSection = document.getElementById("hide-text-area");
  commentSection.style.display = "block";
}

addEventListener("DOMContentLoaded", (event) => {
  const editCommentButtons = document.getElementsByClassName("edit-comment");
  Array.from(editCommentButtons).forEach((element) => {
    element.addEventListener("click", unhideCommentSection);
  });
});
