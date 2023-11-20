'use strict';
// Selecting elements
const todoContainer = document.querySelector('.todo__container');
const todoForm = document.querySelector('.todo__form');
const todoInput = document.querySelector('.todo__form--input');
const errorText = document.querySelector('.error-text');
const todoList = document.querySelector('.todo__list');
const overlayContainer = document.querySelector('.overlay__container');
const overlayText = document.querySelector('.overlay__box--text');
const overlayBox = document.querySelector('.overlay__box');
const overlayBtns = document.querySelector('.overlay__box--btns');
const overlayYesBtn = document.querySelector('.overlay__btn--yes');
const overlayNoBtn = document.querySelector('.overlay__btn--no');

class Todo {
  id = Math.floor(Math.random() * 9999999 + 1);
  date = new Date();
  checked = false;
  constructor(work) {
    this.work = work;
  }
}
class App {
  #todos = [];
  constructor() {
    todoForm.addEventListener('submit', this._formHandler.bind(this));
  }

  _formHandler(e) {
    // e.preventDefault();
    let todo;
    const todoValue = todoInput.value;
    if (!todoValue) {
      errorText.classList.remove('hidden');
    } else {
      errorText.classList.add('hidden');
    }
  }
}

const app = new App();
