"use strict";

var delete_success = document.querySelector('.delete-success'),
    article_delete_button = document.querySelector('.article-delete'),
    delete_cancel = document.querySelectorAll('.delete_cancel'),
    body = document.querySelector('body'); // body.classList.toggle('open')

if (delete_success) {
  article_delete_button.addEventListener('click', function () {
    body.classList.add('open');
    delete_success.style.display = 'flex';
  });
  delete_cancel.forEach(function (element) {
    element.addEventListener('click', function () {
      body.classList.remove('open');
      delete_success.style.display = 'none';
    });
  });
} // --------------------------------


var comments = document.querySelectorAll('.comment');
comments.forEach(function (element) {
  var delete_comment_success = element.querySelector('.delete-comment_success'),
      delete_comment_button = element.querySelector('.delete-comment'),
      delete_comments_cancel = element.querySelectorAll('.delete-comment_cancel');

  if (delete_comment_success) {
    delete_comment_button.addEventListener('click', function () {
      body.classList.add('open');
      delete_comment_success.style.display = 'flex';
    });
    delete_comments_cancel.forEach(function (element2) {
      element2.addEventListener('click', function () {
        body.classList.remove('open');
        delete_comment_success.style.display = 'none';
      });
    });
  }
}); // --------------------------------