# API Documentation: Matrimony Project



## 1. App Name: user_app
This app manages user-related functionalities, including user creation, updates, deletion, authentication, and subscription handling.


### API Endpoints

**1. `GET`: Retrieve All Users**

* Description: Fetches a paginated list of all users.

* URL: `http://127.0.0.1:8000/users/user/`

* Features:
    * Pagination.

    * Returns serialized user details excluding the password.
* Input: No body required.
* Output:
    * `Success (200)`:
    ```json 
    {
    "count": 9,
    "next": "http://127.0.0.1:8000/users/user/?page=2",
    "previous": null,
    "results": [
        {
            "user_id": "AD001",
            "username": "Admin",
            "email": "",
            "first_name": "Admin",
            "last_name": "",
            "role": "admin",
            "subcription_plan": null,
            "join_date": "2024-11-12 04:34:15",
            "last_login": "2024-11-12 05:38:20",
            "created_on": "2024-11-12 04:34:16",
            "updated_on": "2024-11-12 05:02:36",
            "is_active": true,
            "is_admin": false
        },..
    ```
    * `Error (500)`:
    ``` json
    {
    "error": "Internal Server Error"
    }
    ```

**2.`POST`: Create a New User**

* Description: Creates a new user and handles subscription plan activation and notifications.
* URL : `http://127.0.0.1:8000/users/user/`

* Features:
    * Hashes password before saving.
    * Activates subscription and sends notifications.
    * Generates an authentication token for the user.
* Input:
    ``` json 
    {
        "user_id" : "US008",
        "username": "manu",
        "password": "manu123",
        "email": "manu@example.com",
        "first_name": "salman",
        "last_name": "faris",
        "role": "user",
        "subcription_plan":"basic"
    }
    ```
* Output:
    * `Success (201)`:


    ``` json 
    {
    "user": {
        "user_id": "US008",
        "username": "manu",
        "email": "manu@example.com",
        "first_name": "salman",
        "last_name": "faris",
        "role": "user",
        "subcription_plan": "basic",
        "join_date": "2024-11-22 19:07:02",
        "last_login": null,
        "created_on": "2024-11-22 19:07:03",
        "updated_on": "2024-11-22 19:07:03",
        "is_active": true,
        "is_admin": false
    },
    "token": "21076f19dd7f039242dbd3cb71798694c37c7190"
    }
    ```
    * `Error (400)`:
    ```json
    {
    "error": "Invalid subscription plan"
    }
    ```

**3.`GET`: Retrieve User by ID**
* Description: Fetches details of a specific user by their user_id.
* URL: `http://127.0.0.1:8000/users/user/<str:user_id>/`
* Path Parameter: user_id (e.g., /user/123/)
* Features:
    * Fetches user data only if the request is authorized.
* Input: No body required.
* Output:
    * `Success (200)`:
    ```json
    {
        "user_id": "US006",
        "username": "kiran",
        "email": "kiran@example.com",
        "first_name": "alby",
        "last_name": "tommy",
        "role": "user",
        "subcription_plan": "basic",
        "join_date": "2024-11-19 05:00:02",
        "last_login": "2024-11-22 18:16:34",
        "created_on": "2024-11-19 05:00:03",
        "updated_on": "2024-11-22 17:54:25",
        "is_active": true,
        "is_admin": false
    }
    ```
    * `Error (403)`:
    ```json
        {
            "error": "You are not authorized to view this user's information."
        }
    ```
**4.`PUT`: Update User by ID**
* Description: Updates user details.
* URL:`http://127.0.0.1:8000/users/user/<str:user_id>/`
* Body Parameters:
    ```json 
    {
    "user_id": "US004",
    "username": "sachin",
    "email": "sacgin@example.com",
    "password": "sachin123",
    "first_name": "sahin",
    "last_name": "ray",
    "role": "user",
    "subcription_plan": "elite",
    "join_date": "2024-11-18 04:09:13",

    "is_active": true
    }
    ```
* Features:
    * Updates subscription details and durations.
    * updates user deatils
* Output:
    * `Success (200)`:
    ```json
    {
        "user_id": "US004",
        "username": "sachin",
        "email": "sacgin@example.com",
        "first_name": "sahin",
        "last_name": "ray",
        "role": "user",
        "subcription_plan": "elite",
        "join_date": "2024-11-18 04:09:13",
        "last_login": "2024-11-22 18:46:00",
        "created_on": "2024-11-18 04:09:15",
        "updated_on": "2024-11-24 04:45:44",
        "is_active": true,
        "is_admin": false
    }
    ```
    * `Error (404)`:
    ```json
    {
    "error": "User not found"
    }
    ```
**4.DELETE: Delete User by ID**

Description: Deletes a user by inactivating.
* URL: `http://127.0.0.1:8000/users/user/<str:user_id>/`
* Output:
    * `Success (204)`:
     ```json
    {
        "message": "User deleted successfully!"
    }
    ```
**5. Login**
* Method: POST
* Permissions: No authentication required.

* Description: Authenticates a user and generates an authentication token.

* Body Parameters:
``` json
{
    "username": "manu",
    "password": "manu123"
}
```
* Output:
    * `Success (200)`:
    ```json
    {
        "token": "21076f19dd7f039242dbd3cb71798694c37c7190"
    }
    ```
    * `Error (400)`:
    ``` json
    {
        "detail": "Invalid credentials"
    }
    ```
**6. Logout**
* Method: POST
* Permissions: Requires authentication.
* Description: Logs out the user by deleting their token.
* Output:
    * Success (200):
    ```json
    {
        "detail": "Successfully logged out."
    }
    ```
    * `Error (400)`:
    ```json
    {
        "detail": "No active session to logout."
    }
    ```



---

## 2.App Name: profile_app

This app manages user profiles in the matrimony project. Each user has a profile containing personal and demographic details. The APIs allow for profile creation, retrieval, updates, and deletion.

### API Endpoints

**1. GET: Retrieve all user profiles**

* Description: Fetches the list of all user profiles.


* URL: `http://127.0.0.1:8000/profiles/profiles/`
* Permission: Authenticated users only.
* Output:

    * `Success (200)`:
    ```json
    [
        {
            "id": 1,
            "created_on": "2024-11-13 06:56:33",
            "updated_on": "2024-11-19 06:54:25",
            "age": 24,
            "gender": "male",
            "dob": "2000-01-10",
            "bio": "famly guy",
            "weight": "59.00",
            "height": "5.70",
            "religion": "Christianity",
            "caste": "OBC (Other Backward Class)",
            "income": "60000.00",
            "profession": "Software Engineer",
            "education": "Bachelor of Science",
            "location": "Tamil Nadu",
            "marital_status": "single",
            "language": "Tamil",
            "address": "vdakanchery,palakkad,kerala",
            "image": "/media/profile_images/profile-picture_oTRqlHF.jpeg",
            "user": "US001"
        },..
   ]
   ```
**2.POST: Create User Profile**
* Description: Creates a new user profile and associates it with the authenticated user. Sends notifications if matching scores with preferences are found.
* URL: `http://127.0.0.1:8000/profiles/profiles/`
* Body Parameters:
    ``` json
    {
        "user":"US007",
        "dob": "1997-1-10",
        "location": "Tamil Nadu",
        "education": "Master of Education",
        "profession": "Software Engineer",
        "caste": "Maratha",
        "religion": "Christianity",
        "gender": "male",
        "marital_status": "single",
        "language": "Tamil",
        "height": 6.9,
        "weight": 67,
        "income": 900000


    }
    ```
* Features:

    * Validates and saves the profile.
    * Automatically calculates the user's age based on the date of birth (dob).
    * Checks for matching scores with existing preferences and sends notifications for significant matches.
* Output:
    * `Success (201)`:
    ``` json
    {
    "user_profile": {
        "id": 28,
        "age": 27,
        "gender": "male",
        "dob": "1997-01-10",
        "bio": null,
        "weight": "67.00",
        "height": "6.90",
        "religion": "Christianity",
        "caste": "Maratha",
        "income": "900000.00",
        "profession": "Software Engineer",
        "education": "Master of Education",
        "location": "Tamil Nadu",
        "marital_status": "single",
        "language": "Tamil",
        "address": null,
        "image": null,
        "created_on": "2024-11-21T07:30:39.327632Z",
        "updated_on": "2024-11-21T07:30:39.327658Z",
        "user": "US007"
        }
    }
    ```
  * `Error (400)`:
    ```json
    {
        "error": "A profile already exists for this user."
    }
    ```
**3. GET: Retrieve User Profile by ID**
* Description: Retrieves a specific user profile by user ID.


* URL:`http://127.0.0.1:8000/profiles/profiles/<str:user_id>/`
* Body Parameters: None.

* Features:

    * Ensures the requesting user has permission to view the specified profile.
* Output:

    * Success (200):

    ```json
    {
        "id": 5,
        "created_on": "2024-11-18 07:43:24",
        "updated_on": "2024-11-19 06:54:25",
        "age": 34,
        "gender": "female",
        "dob": "1990-01-29",
        "bio": "suportive person",
        "weight": "67.00",
        "height": "6.90",
        "religion": "Islam",
        "caste": "General",
        "income": "90000.00",
        "profession": "Software Engineer",
        "education": "Master of Education",
        "location": "Tamil Nadu",
        "marital_status": "widowed",
        "language": "Tamil",
        "address": "ramashoram,tamil nadu,india",
        "image": "http://127.0.0.1:8000/media/profile_images/profile-picture_7NGCwCV.jpeg",
        "user": "US005"
    }
    ```

    * `Error (404)`:
    ```json
    {
        "error": "User profile not found."
    }
    ```
**4.PUT: Update User Profile by ID**

* Description: Updates a specific user profile.
* URL:`http://127.0.0.1:8000/profiles/profiles/<str:user_id>/`
* Body Parameters:
    ```json
    {

        "dob": "1990-01-29",
        "address": "ramashoram,tamil nadu,india",
        "religion": "Islam",
        "caste": "General",
        "gender": "male"
    }
    ```
* Features:
    * Validates the updated details.
    * Automatically recalculates the user's age if the dob is updated.
* Output:


    * Success (200):
    ```json
    {
        "id": 5,
        "created_on": "2024-11-18 07:43:24",
        "updated_on": "2024-11-24 08:34:11",
        "age": 34,
        "gender": "male",
        "dob": "1990-01-29",
        "bio": "suportive person",
        "weight": "67.00",
        "height": "6.90",
        "religion": "Islam",
        "caste": "General",
        "income": "90000.00",
        "profession": "Software Engineer",
        "education": "Master of Education",
        "location": "Tamil Nadu",
        "marital_status": "widowed",
        "language": "Tamil",
        "address": "ramashoram,tamil nadu,india",
        "image": "http://127.0.0.1:8000/media/profile_images/profile-picture_7NGCwCV.jpeg",
        "user": "US005"
    }
    ```
    * `Error (403)`:
    ```json
    {
        "error": "Permission denied."
    }
    ```
    * `Error (404)`:
    ```json
    {
        "error": "User profile not found."
    }
    ```
**5.DELETE: Delete User Profile by ID**
* Description: Deletes a specific user profile.
* URL:`http://127.0.0.1:8000/profiles/profiles/<str:user_id>/`
* Features:
    * Ensures the requesting user has permission to delete the profile.

* Output:
    * `Success (204)`:No Content.
    * `Error (403)`:
    ```json
        {
        "error": "Permission denied."
        }
    ```
    * `Error (404)`:
    ```json
    {
        "error": "User profile not found."
    }
    ```
## 3.APP NAME: Preference App

**1. GET: List All Preferences**
* Description: Retrieves a list of all preferences for all users.
* URL:`http://127.0.0.1:8000/preferences/preference/`
* Method: GET
* Headers:
```json
{
    "Authorization": "Token <user_token>"
}
```

* Features:
    * Displays all preferences.
    * Requires authentication.
* Output:
    * Success (200):
    ```json
    {
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "created_on": "2024-11-14 06:12:47",
            "updated_on": "2024-11-19 05:40:40",
            "age_range": {
                "from": 25,
                "to": 40
            },
            "income_range": {
                "from": 50000.0,
                "to": 100000.0
            },
            "height_range": {
                "from": 5.5,
                "to": 7.0
            },
            "weight_range": {
                "from": 60.0,
                "to": 80.0
            },
            "gender": "female",
            "religion": [
                "Christianity",
                "Hinduism"
            ],
            "caste": [
                "General",
                "OBC (Other Backward Class)"
            ],
            "profession": [
                "Software Engineer",
                "Doctor"
            ],
            "education": [
                "Master of Education",
                "Bachelor of Science"
            ],
            "location": [
                "Kerala",
                "Tamil Nadu"
            ],
            "language": [
                "Malayalam",
                "Tamil"
            ],
            "marital_status": [
                "single",
                "divorced",
                "widowed"
            ],
            "user": "US001"
        },
    ]
    }
    ```
**2. POST: Create a New Preference**
* Description: Creates a new preference for the authenticated user.
* URL: `http://127.0.0.1:8000/preferences/preference/`
* Method: POST
* Headers:
```json
{
    "Authorization": "Token <user_token>"
}
```
* Body Parameters:
```json
{
  "user": "US008",
  "age_range": {"from": 20,"to": 30},
  "gender": "male",
  "religion": ["Judaism","Zoroastrianism"],
  "caste": ["Vaisya", "Maratha"],
  "income_range": {
    "from": 80000.00,
    "to": 1000000.00
  },
  "profession": ["Data Scientist", "Pharmacist"],
  "education": ["Master of Technology", "Doctor of Philosophy (PhD)"],
  "location": ["Nagaland", "Odisha"],
  "height_range": {
    "from": 6.0,
    "to": 9.0
  },
  "weight_range": {
    "from": 50.0,
    "to": 100.0
  }

}
```

* Features:


    * Automatically links the preference to the authenticated user.

* Output:
    * Success (201):
    ```json
    {
        "id": 6,
        "created_on": "2024-11-24 15:31:48",
        "updated_on": "2024-11-24 15:31:48",
        "age_range": {
            "from": 20,
            "to": 30
        },
        "income_range": {
            "from": 80000.0,
            "to": 1000000.0
        },
        "height_range": {
            "from": 6.0,
            "to": 9.0
        },
        "weight_range": {
            "from": 50.0,
            "to": 100.0
        },
        "gender": "male",
        "religion": [
            "Judaism",
            "Zoroastrianism"
        ],
        "caste": [
            "Vaisya",
            "Maratha"
        ],
        "profession": [
            "Data Scientist",
            "Pharmacist"
        ],
        "education": [
            "Master of Technology",
            "Doctor of Philosophy (PhD)"
        ],
        "location": [
            "Nagaland",
            "Odisha"
        ],
        "language": null,
        "marital_status": null,
        "user": "US006"
    }
    ```
    * `Error (400)`:
    ```json
    {
        "error": "Validation failed for one or more fields."
    }
    ```
**3. GET: Retrieve User Preference**
* Description: Fetches the preference details for a specific user.
* URL: `http://127.0.0.1:8000/preferences/preference/US001/`
* Method: GET
* Headers:
```json
{
    "Authorization": "Token <user_token>"
}
```
* Features:

    * Returns the preference details for the user.
    * Ensures the authenticated user can only access their own preferences.
* Output:
    * Success (200):
    ```json
    {
        "id": 1,
        "created_on": "2024-11-14 06:12:47",
        "updated_on": "2024-11-19 05:40:40",
        "age_range": {
            "from": 25,
            "to": 40
        },
        "income_range": {
            "from": 50000.0,
            "to": 100000.0
        },
        "height_range": {
            "from": 5.5,
            "to": 7.0
        },
        "weight_range": {
            "from": 60.0,
            "to": 80.0
        },
        "gender": "female",
        "religion": [
            "Christianity",
            "Hinduism"
        ],
        "caste": [
            "General",
            "OBC (Other Backward Class)"
        ],
        "profession": [
            "Software Engineer",
            "Doctor"
        ],
        "education": [
            "Master of Education",
            "Bachelor of Science"
        ],
        "location": [
            "Kerala",
            "Tamil Nadu"
        ],
        "language": [
            "Malayalam",
            "Tamil"
        ],
        "marital_status": [
            "single",
            "divorced",
            "widowed"
        ],
        "user": "US001"
    }
    ```
    * Error (404):
    ```json
    {
        "error": "Preference not found for user."
    }
    ```
**4. PUT: Update User Preference**
* Description: Updates the preference details for a specific user.
* URL: `http://127.0.0.1:8000/preferences/preference/US001/`
* Method: PUT
* Headers:
```json
{
    "Authorization": "Token <user_token>"
}
```
* Body Parameters:
```json
{
    "id": 1,
    "age_range": {
        "from": 25,
        "to": 40
    },
    "income_range": {
        "from": 50000.0,
        "to": 100000.0
    },
    "height_range": {
        "from": 5.5,
        "to": 7.0
    },
    "weight_range": {
        "from": 60.0,
        "to": 80.0
    },
    "gender": "female",
    "religion": [
        "Christianity",
        "Hinduism"
    ],
    "caste": [
        "General",
        "OBC (Other Backward Class)"
    ],
    "profession": [
        "Software Engineer",
        "Doctor"
    ],
    "education": [
        "Master of Education",
        "Bachelor of Science"
    ],
    "location": [
        "Kerala",
        "Tamil Nadu"
    ],
    "marital_status": ["single"],

    "created_on": "2024-11-14T06:12:47.565658Z",
    "updated_on": "2024-11-14T06:12:47.565713Z",
    "user": "US001",
    "langauge": [
        "Malayalam",
        "Tamil"
    ]
}
```
* Features:

    * Ensures only the authenticated user can update their own preferences.
* Output:
    * Success (200):
    ```json
    {
        "id": 1,
        "created_on": "2024-11-14 06:12:47",
        "updated_on": "2024-11-24 15:43:47",
        "age_range": {
            "from": 25,
            "to": 40
        },
        "income_range": {
            "from": 50000.0,
            "to": 100000.0
        },
        "height_range": {
            "from": 5.5,
            "to": 7.0
        },
        "weight_range": {
            "from": 60.0,
            "to": 80.0
        },
        "gender": "female",
        "religion": [
            "Christianity",
            "Hinduism"
        ],
        "caste": [
            "General",
            "OBC (Other Backward Class)"
        ],
        "profession": [
            "Software Engineer",
            "Doctor"
        ],
        "education": [
            "Master of Education",
            "Bachelor of Science"
        ],
        "location": [
            "Kerala",
            "Tamil Nadu"
        ],
        "language": [
            "Malayalam",
            "Tamil"
        ],
        "marital_status": "single",
        "user": "US001"
    }
    ```
    * Error (403):
    ```json
    {
        "error": "Permission denied. You can only update your own preferences."
    }
    ```
**5. DELETE: Delete User Preference**
* Description: Deletes the preference for a specific user.
* URL:`http://127.0.0.1:8000/preferences/preference/US001/`
* Method: DELETE
* Headers:
```json
{
    "Authorization": "Token <user_token>"
}
```
* Features:
    * Ensures only the authenticated user can delete their own preferences.
* Output:
    * Success (204):No Content

    * Error (403):
    ```json
    {
        "error": "Permission denied. You can only delete your own preferences."
    }
    ```





---
## APP NAME: Common Matching App


### 1. GET: List All Matching Options
* **Description:** Retrieves a list of all common matching fields from the master table.
* **URL:** `http://127.0.0.1:8000/master_table/common-matching/`
* **Method:** GET
* **Headers:**
```json
{
    "Authorization": "Token <admin_user_token>"
}
```
* **Features:**
    * Displays all matching options.
    * Requires admin authentication.

* **Output:**
    * **Success (200):**
    ```json
    [
        {
            "id": 1,
            "type": "gender",
            "code": "GN001",
            "name": "Male",
            "display_name": "Male"
        },
        {
            "id": 2,
            "type": "religion",
            "code": "RE001",
            "name": "Christianity",
            "display_name": "Christian"
        }
    ]
    ```

---

### 2. POST: Add a New Matching Option
* **Description:** Adds a new entry to the `Common_Matching` master table and sends notifications to all users about the addition.
* **URL:** `http://127.0.0.1:8000/master_table/common-matching/`
* **Method:** POST
* **Headers:**
```json
{
    "Authorization": "Token <admin_user_token>",
    "Content-Type": "application/json"
}
```
* **Body Example:**
```json
{
    "type": "caste",
    "name": "General",
    "display_name": "General Category"
}
```
* **Features:**
    * Adds a new matching option.
    * Sends notifications to all users about the addition.
    * Requires admin authentication.

* **Output:**
    * **Success (201):**
    ```json
    {
        "new option is created and notifications sent to all users!": {
            "id": 3,
            "type": "caste",
            "code": "CA001",
            "name": "General",
            "display_name": "General Category"
        }
    }
    ```

---

### 3. GET: Retrieve Options by Type
* **Description:** Retrieves all matching options for a specific field type.
* **URL:** `http://127.0.0.1:8000/master_table/options/<field_type>/`
* **Method:** GET
* **Headers:**
```json
{
    "Authorization": "Token <admin_user_token>"
}
```
* **Path Parameters:**
    * `field_type`: Type of the field (e.g., `gender`, `religion`, `caste`, etc.).

* **Features:**
    * Retrieves options filtered by field type.
    * Requires admin authentication.

* **Output:**
    * **Success (200):**
    ```json
    [
        {
            "id": 1,
            "type": "gender",
            "code": "GN001",
            "name": "Male",
            "display_name": "Male"
        },
        {
            "id": 2,
            "type": "gender",
            "code": "GN002",
            "name": "Female",
            "display_name": "Female"
        }
    ]
    ```
    * **Error (400):**
    ```json
    {
        "error": "Invalid field type"
    }
    ```

---

### 4. GET/PUT/PATCH/DELETE: Manage Specific Matching Option
* **Description:** Retrieve, update, or delete a specific matching option by ID.
* **URL:** `http://127.0.0.1:8000/master_table/common-matching/<int:pk>/`
* **Methods:** GET, PUT, DELETE
* **Headers:**
```json
{
    "Authorization": "Token <admin_user_token>"
}
```
* **Path Parameters:**
    * `pk`: ID of the matching option.

* **Features:**
    * Retrieve, update, or delete a specific matching option.
    * Requires admin authentication.

* **Output:**
    * **GET Success (200):**
    ```json
    {
        "id": 3,
        "type": "caste",
        "code": "CA001",
        "name": "General",
        "display_name": "General"
    }
    ```
    * **PUT Success (200):**
    ```json
    {
        "id": 3,
        "type": "caste",
        "code": "CA001",
        "name": "General",
        "display_name": "General "
    }
    ```
    * **DELETE Success (204):**
    No Content.


---
## APP NAME: Matching App 




### 1. Calculate Matching Score

**Description:** Calculate the matching score between two users based on their preferences and profile data.

- **URL:** `(http://127.0.0.1:8000/maching/calculate_matching_score/)`
- **Method:** POST
- **Headers:**
  ```json
  {
      "Authorization": "Token <user_token>"
  }
  ```
- **Request Body:**
  ```json
  {
      "user1_id": "<string>",
      "user2_id": "<string>"
  }
  ```
- **Features:**
  - Validates that `user1` and `user2` are not the same user.
  - Ensures both `user1_id` and `user2_id` exist in the database.
  - Calculates and stores the matching score between `user1` and `user2`.
  - Creates a match request notification for `user2`.

- **Responses:**
  - **Success (200):**
    ```json
    {
        "user1": "USER001",
        "user2": "USER002",
        "status": "Pending",
        "score": 85.0,
        "user2_profile": {
            "id": 2,
            "name": "John Doe",
            "age": 30,
            ...
        },
        "created_on": "2024-11-24 08:30:00",
        "updated_on": "2024-11-24 08:30:00"
    }
    ```

  - **Error (400):**
    ```json
    {
        "error": "User cannot be matched with themselves."
    }
    ```

  - **Error (404):**
    ```json
    {
        "error": "User not found."
    }
    ```

---

### 2. Get Recommended Matching Scores for a User
**Description:** Get all matching scores for a given user, ordered by score in descending order.

- **URL:** `http://127.0.0.1:8000/maching/recomended_users_for/<user_id>/`
- **Method:** POST
- **Headers:**
  ```json
  {
      "Authorization": "Token <user_token>"
  }
  ```
- **Request Body:** None

- **Features:**
  - Retrieves all users excluding the requesting user (`user_id`).
  - Calculates and stores matching scores between the given user and all other users.
  - Returns the matching scores in descending order.

- **Responses:**
  - **Success (200):**
    ```json
    [
      {
        "user1": "USER001",
        "user2": "USER002",
        "status": "Pending",
        "score": 95.0,
        "user2_profile": {
            "id": 2,
            "name": "John Doe",
            "age": 30,
            ...
        },
        "created_on": "2024-11-24 08:30:00",
        "updated_on": "2024-11-24 08:30:00"
      },
      ...
    ]
    ```

  - **Error (404):**
    ```json
    {
        "error": "User not found."
    }
    ```

---

### 3. Update Matching Status
**Description:** Update the status of a matching record between two users.

- **URL:** `http://127.0.0.1:8000/maching/update_matching_status/<user1>/<user2>/`
- **Method:** PUT
- **Headers:**
  ```json
  {
      "Authorization": "Token <user_token>"
  }
  ```
- **Request Body:**
  ```json
  {
      "status": "<string>"
  }
  ```
  - **Status Options:** `Rejected`, `Accepted`, `Pending`

- **Features:**
  - Validates that the authenticated user can update the matching status.
  - Sends notifications based on the status change (Accepted/Rejected/Request).

- **Responses:**
  - **Success (200):**
    ```json
    {
        "user1": "USER001",
        "user2": "USER002",
        "status": "Accepted",
        "score": 85.0,
        "user2_profile": {
            "id": 2,
            "name": "John Doe",
            "age": 30,
            ...
        },
        "created_on": "2024-11-24 08:30:00",
        "updated_on": "2024-11-24 08:30:00"
    }
    ```

  - **Error (403):**
    ```json
    {
        "error": "You are not authorized to update this match status."
    }
    ```

  - **Error (404):**
    ```json
    {
        "error": "Matching record not found."
    }
    ```

  - **Error (400):**
    ```json
    {
        "error": "Invalid status."
    }
    ```

---

## APP NAME: Subscription App

### 1. GET: List All Subscription Types
**Description:** Retrieves a list of all available subscription types.  
**URL:** `http://127.0.0.1:8000/subcriptions/subcription/`  
**Method:** GET  
**Headers:**
```json
{
    "Authorization": "Token <admin_user_token>"
}
```
**Features:**
- Displays all available subscription types.
- Requires admin authentication for creating or updating subscription types.
  
**Output:**

**Success (200):**
```json
[
    {
        "subcription_type": "Basic",
        "subcription_price": 100,
        "subcription_duration": 30,
        "subcription_active_status": true
    },
    {
        "subcription_type": "Premium",
        "subcription_price": 250,
        "subcription_duration": 60,
        "subcription_active_status": true
    }
]
```



### 2. POST: Create a New Subscription Type
**Description:** Creates a new subscription type and sends notifications to all users about the new subscription.  
**URL:** `http://127.0.0.1:8000/subcriptions/subcription/`  
**Method:** POST  
**Headers:**
```json
{
    "Authorization": "Token <admin_user_token>"
}
```
**Request Body:**
```json
{
    "subcription_type": "Standard",
    "subcription_price": 150,
    "subcription_duration": 45,
    "subcription_active_status": true
}
```

**Features:**
- Requires admin authentication.
- Sends a notification to all users regarding the new subscription.

**Output:**

**Success (201):**
```json
{
    "Subscription created and notifications sent to all users!": {
        "subcription_type": "Standard",
        "subcription_price": 150,
        "subcription_duration": 45,
        "subcription_active_status": true
    }
}
```



### 3. GET: Retrieve Subscription by Type
**Description:** Retrieve details of a specific subscription type by its `subcription_type`.  
**URL:** `http://127.0.0.1:8000/subcription/<str:subcription_type>/`  
**Method:** GET  
**Headers:**
```json
{
    "Authorization": "Token <admin_user_token>"
}
```

**Features:**
- Retrieve specific subscription details by type.
  
**Output:**

**Success (200):**
```json
{
    "subcription_type": "Standard",
    "subcription_price": 150,
    "subcription_duration": 45,
    "subcription_active_status": true
}
```

---

### 4. PUT: Update a Subscription Type
**Description:** Update an existing subscription type.  
**URL:** `http://127.0.0.1:8000/subcriptions/subcription/<str:subcription_type>/`  
**Method:** PUT  
**Headers:**
```json
{
    "Authorization": "Token <admin_user_token>"
}
```
**Request Body:**
```json
{
    "subcription_price": 200,
    "subcription_duration": 60
}
```

**Features:**
- Update an existing subscription type by its `subcription_type`.
- Requires admin authentication.

**Output:**

**Success (200):**
```json
{
    "subcription_type": "Standard",
    "subcription_price": 200,
    "subcription_duration": 60,
    "subcription_active_status": true
}
```



### 5. DELETE: Delete a Subscription Type
**Description:** Delete a specific subscription type by its `subcription_type`.  
**URL:** `http://127.0.0.1:8000/subcriptions/subcription/<str:subcription_type>/`  
**Method:** DELETE  
**Headers:**
```json
{
    "Authorization": "Token <admin_user_token>"
}
```

**Features:**
- Delete a subscription type by `subcription_type`.
- Requires admin authentication.

**Output:**

**Success (204):**
```json
{
    "detail": "Not found."
}
```

---

### 6. GET: List All Subscriptions for Users( Subcription History )
**Description:** Lists all subscriptions assigned to users.  
**URL:** `http://127.0.0.1:8000/subcriptions/subcription_list/`  
**Method:** GET  
**Headers:**
```json
{
    "Authorization": "Token <user_token>"
}
```
**Features:**
- Displays all subscriptions assigned to users.

**Output:**

**Success (200):**
```json
[
    {
        "subcription_id": 1,
        "subcription_type": "Standard",
        "user_id": 1,
        "subcription_started_at": "2024-11-24T12:00:00",
        "subcription_ending_at": "2024-12-09T12:00:00",
        "subcription_active_status": true
    },
    {
        "subcription_id": 2,
        "subcription_type": "Premium",
        "user_id": 2,
        "subcription_started_at": "2024-11-23T09:30:00",
        "subcription_ending_at": "2024-12-23T09:30:00",
        "subcription_active_status": true
    }
]
```
---
## APP NAME: message_app

### 1. POST: Create Message
**Description**: Creates a new message and sends a notification to the receiver.  
**URL**:`http://127.0.0.1:8000/messages/message/` 
**Method**: POST

**Headers**:
```json
{
    "Authorization": "Token <admin_user_token>"
}
```
**Request Body**:
```json
{
    "receiver_id": "<receiver_user_id>",
    "message_content": "<message_content>"
}
```
**Features**:
* Allows authenticated users to send a message to another user.

* Creates a notification for the receiver upon sending the message.

**Output:**

  * Success (201):
  
    ```json
    {
        "message_id": 17,
        "created_at": "2024-11-24T17:57:49.533179Z",
        "updated_at": "2024-11-24T17:57:49.533209Z",
        "message_content": "hi akshay",
        "is_read": false,
        "sender_id": "US001",
        "receiver_id": "US006"
    }
    ```
### 2. GET: Get Messages by Receiver
* Description: Retrieves a list of messages sent to a specific user (receiver).
* URL:`http://127.0.0.1:8000/messages/new_message/str:receiver_id/`
* Method: GET
* Headers:
```json
{
    "Authorization": "Token <admin_user_token>"
}
```

* Features:

  * Retrieves both unread and read messages for the specified receiver.
  * Marks all unread messages as read after sending the response.
* Output:

    * Success (200):
    ```json
    {
        "unread messages": [
            {
                "message_id": 17,
                "created_at": "2024-11-24T17:57:49.533179Z",
                "updated_at": "2024-11-24T17:57:49.533209Z",
                "message_content": "hi akshay",
                "is_read": false,
                "sender_id": "US001",
                "receiver_id": "US006"
            }
        ],
        "read messages": [
            {
                "message_id": 16,
                "created_at": "2024-11-22T19:08:26.143228Z",
                "updated_at": "2024-11-22T19:08:26.143283Z",
                "message_content": "hi akshay",
                "is_read": true,
                "sender_id": "US001",
                "receiver_id": "US006"
            },
            {
                "message_id": 15,
                "created_at": "2024-11-20T17:46:24.883521Z",
                "updated_at": "2024-11-20T17:46:24.883558Z",
                "message_content": "hi bro",
                "is_read": true,
                "sender_id": "US001",
                "receiver_id": "US006"
            }
        ]
    }
    ```
---


## APP NAME: notification_app

### 1. POST: Create Notification
**Description**: Creates a new notification and sends it to the receiver.  
**URL**:`http://127.0.0.1:8000/notifications/notification/`  
**Method**: POST

**Headers**:
```json
{
    "Authorization": "Token <admin_user_token>"
}
```
* Request Body:

```json
{
    "notification_type": "new_message",
    "notification_message": "<message_content>",
    "sender_id": "<sender_user_id>",
    "receiver_id": "<receiver_user_id>"
}
```
* Features:
    * Allows authenticated users to create notifications.
    * Notification types can be one of: reminder, new_message, new_match, offer, profile, preference, rejected, accepted, request.
    * Notifications are associated with a sender and a receiver.
* Output:
    * Success (201):
    ```json
    {
        "notification_id": 194,
        "notification_date": "2024-11-24 18:18:20",
        "created_at": "2024-11-24 18:18:20",
        "updated_at": "2024-11-24 18:18:20",
        "notification_type": "new_message",
        "notification_message": "you have a new maching",
        "is_read": false,
        "sender_id": "US002",
        "receiver_id": "US001"
    }
    ```
### 2. GET: Get Notifications by Receiver
* Description: Retrieves a notification by its type.
* URL:`http://127.0.0.1:8000/notifications/new_notification/US006/`
* Method: GET

* Headers:
```json
{
    "Authorization": "Token <user_token>"
}
```
* Features:

    * Retrieves unread and read notifications for a specified receiver (user).
    * Ensures the authenticated user is the same as the receiver (user).
    * Marks all unread notifications as read after retrieving.

* Output:

    * Success (200):
    ```json
    {
        "unread messages": [
            {
                "notification_id": 193,
                "notification_date": "2024-11-24 17:57:49",
                "created_at": "2024-11-24 17:57:49",
                "updated_at": "2024-11-24 17:57:49",
                "notification_type": "new_message",
                "notification_message": "US001 has sent you a message. Check it now!",
                "is_read": false,
                "sender_id": "US001",
                "receiver_id": "US006"
            }
        ],
        "read messages": [
            {
                "notification_id": 192,
                "notification_date": "2024-11-22 19:08:26",
                "created_at": "2024-11-22 19:08:26",
                "updated_at": "2024-11-22 19:08:26",
                "notification_type": "new_message",
                "notification_message": "US001 has sent you a message. Check it now!",
                "is_read": true,
                "sender_id": "US001",
                "receiver_id": "US006"
            }
    }
    ```
    * Unauthorized Access (403 Forbidden):
    ```json
    {
        "detail": "You are not authorized to view these messages."
    }
    ```
    * Invalid Receiver ID (404 Not Found):
    ```json
    {
        "detail": "The specified receiver does not exist."
    }
    ```
    * Bad Request (400 Bad Request):
    ```json
    {
        "detail": "Receiver ID is required and must be a valid user ID."
    }
    ```


## Notification 



| **#** | **App Name**         | **Notification Type** | **Notification Content**                                                                  | **From (Sender)**      | **To (Receiver)**       |
|-------|-----------------------|-----------------------|------------------------------------------------------------------------------------------|------------------------|-------------------------|
| 1     | **Message_app**       | New_Message          | "US001 has sent you a message. Check it now!"                                            | User (e.g., US001)     | User (e.g., US006)      |
| 2     | **User_app**          | Reminder             | "A new user found! 'username' has joined the platform."                                  | System/Admin           | All Existing Users      |
| 3     | **Subscription_app**  | Offer                | "New Offer! A new subscription 'subscription_type' is now available. Check it out!"      | Admin/System           | Specific User           |
| 4     | **Master_app**        | Reminder             | "New {master_table.type} option '{master_table.name}' added by Admin. Update your profile and preferences now!" | Admin/System | Specific User           |
| 5     | **Matching**          | Request              | "[User1] has sent you a match request."                                                  | User (e.g., US001)     | User (e.g., US002)      |
| 6     | **Matching**          | Accepted             | "[User2] has accepted your match request."                                              | User (e.g., US002)     | User (e.g., US001)      |
| 7     | **Matching**          | Rejected             | "[User2] has rejected your match request."                                              | User (e.g., US002)     | User (e.g., US001)      |
| 8     | **Subscription_app**  | Reminder             | "🎉 Your subscription plan '[subscription_plan]' is officially activated! 💍 ..."        | System                 | Specific User           |
| 9     | **Profile_app**       | Profile              | "A new match found! '[request.user.username]' has joined the platform with a matching score of [score]%." | User (e.g., User001)   | User (e.g., User002)    |
| 10    | **Subscription_app**  | Subscription             | "🎉 Your subscription plan '[subscription_plan]' has been reactivated! You've got [days_left] days left. Enjoy your experience! 😊" | System | Specific User |
