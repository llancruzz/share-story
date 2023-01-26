# Testing Instructions
![Manual Testing](media/testing.png)

## Table of Contents

- [Navigation](#navigation)
- [CRUD](#crud)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
- [Sign Up](#sign-up)
- [Log In](#log-in)
- [Log Out](#log-out)
- [Likes](#likes)
- [Social Links](#social-links)

### Methodology

Manual testing occurred regularly throughout local development, making use of statements that would print information to the console and use of the Django debug pages.

### Navigation

All navigation links, including home icon, can be found in navbar or on small to medium screens in the burger drop-down menu.

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Home Link Icon | 1 | While not on homepage, click icon. | User is redirected back to homepage. | PASS |
| "Login" Link | 2 | While not authenticated, click "Login". | User is directed to Login form. | PASS |
| "Sign Up" Link | 3 | While not authenticated, click "Sign Up".| User is directed to Sign Up form. | PASS |
| "Logout" Link | 4 | While authenticated, click "Logout". | User is directed to page with Sign Out button. | PASS |
| "About Us" Link | 5 | Click "About Us" | An informative page will be displayed so that the user understands the purpose of the website | PASS |
| "Share Story" Btn-Link | 6 | Click "Share Your Story" | An informative page will be displayed to the user, informing new features and functionalities. | PASS |

### CRUD

The full CRUD functionality is only available to authenticated users.

#### Create

Write and submit a comment on Leave Comment to submit the comment (authenticated users only).

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Comment field | 1 | Select the empty field and start typing. | Written text displays.| PASS |
| Submit | 2 | After completing Comment form, click submit button. | Alert message informs user of successful submission. The user is directed to the posting page with a newly sent alert message to be approved. | PASS |

#### Read

Read submitted haikus, including tanka extensions (available to all users).

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Post | 1 | On the home page, click on one of the provided posts.| Users can see and read posts posted by the admin with photos and titles. | PASS |
| Comment | 2 | After being approved by the admin.| Users can see and read their posts | PASS |

#### Update

Option to edit existing comments (authenticated users only).

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Edit-Btn | 1 | Click the edit button below the comment body. The button is only visible after login and after the comment has been approved by the admin. | A new text field with a save button will appear. | PASS |
| Save-Btn | 2 | Once you have changed the comment, click on the save button. | After saving the new comment, the message will be changed after admin approval. A message waiting for comment approval would be displayed. | PASS |

#### Delete

Option to delete existing haikus via haiku detail view (authenticated users only).

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Delete-Btn | 1 | Click delete button below comment body. Button is only visible after loggin and after the comment has been approved by the admin. | User is directed to delete page which prompts user to confirm delete action. | PASS |
| Confirm Delete | 2 | On delete page, click "Delete". | Alert message informs user of successful deletion. User is re-directed to post page, selected comment has been deleted. | PASS |
| Cancel-Btn | 3 | On delete page, click "Cancel". | User is re-directed to post page with no delete action taken. | PASS |

### Sign Up

Account creation for unauthenticated users.

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Sign Up Form | 1 | Go to Sign Up page via nav link | Renders form input fields Username, Email (optional), Password, Password (confirm). | PASS |
| Submit | 2 | Fill in form fields accordingly. Click "Sign Up". | Self-closing message informs user of successfull account creation, including username. User is re-directed to homepage and navigation shows links for authenticated users. | PASS |
| Incomplete Form | 3 | Failing to fill out all form fields, click "Sign Up". | User remains on Sign Up form view and is prompted to complete missing fields. | PASS |

### Log In

Signing into existing account (authenticated users only).

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Login Form | 1 | Go to Login page via nav link | Renders form input fields Username, Password, Remember me (checkbox). | PASS |
| Submit | 2 | Fill in form fields accordingly. Click "Sign In". | Self-closing message informs user of successfull login, including username. User is re-directed to homepage and navigation shows links for authenticated users. | PASS |
| Incomplete Form | 3 | Failing to fill out all form fields, click "Sign In". | User remains on Sign Up form view and is prompted to complete missing fields. | PASS |
| Remember Me | 4 | When signing in, tick "Remember me". Logout and sign in again. | Login form is pre-populated with username and hidden password. | PASS |

### Log Out

Allows user to sign out of existing account (authenticated users only).

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Logout Form | 1 | When authenticated, go to Logout page via nav link | User is directed to Logout page, asking user to confirm action. | PASS |
| Sign Out | 2 | On Logout page, click "Sign Out". | Self-closing message informs user of successfull logout. User is re-directed to homepage and navigation shows links for unauthenticated users. | PASS |

### Likes

Option to like/unlike haikus (authenticated users only).

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Like | 1 | Click like button (heart icon) below post body that isn't already liked. | Icon color changes from black to red. Like count is incremented by 1. | PASS |
| Unlike | 2 | Click like button (heart icon) below post body that is already liked. | Icon color changes from red to black. Like count is decremented by 1. | PASS |

### Social Links

Links to social media sites located in footer (available to all users).

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Link Icons in Footer | 1 | Click on any of the social media icons | New tab opens with respective social media site | PASS |


Return to [README.md](README.md)