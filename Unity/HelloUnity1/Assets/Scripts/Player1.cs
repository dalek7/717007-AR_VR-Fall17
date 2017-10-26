using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player1 : MonoBehaviour
{

    public float speed;
    private Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        speed = 10;
    }


    void FixedUpdate()
    {

#if UNITY_ANDROID
		Vector2 touchDeltaPosition = Input.GetTouch(0).deltaPosition;

		float moveHorizontal 	= -0.01f * touchDeltaPosition.x;
		float moveVertical 		= -0.01f * touchDeltaPosition.y;

#else

        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

#endif

        Vector3 movement = new Vector3(moveHorizontal, 0, moveVertical);
        rb.AddForce(movement * speed);

    }
}
