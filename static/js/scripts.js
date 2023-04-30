// Function created to update the comment

function unhideCommentSection(event) {
  const editButton = event.target;
  const commentSection = editButton.previousElementSibling;
  commentSection.style.display = "block";
}

addEventListener("DOMContentLoaded", (event) => {
  const editCommentButtons = document.getElementsByClassName("edit-comment");
  Array.prototype.forEach.call(editCommentButtons, function (element) {
    element.addEventListener("click", unhideCommentSection);
  });
});
