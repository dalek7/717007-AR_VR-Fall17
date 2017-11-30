using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Player1 : MonoBehaviour
{
    int cnt1;
    public Text cntText1;
    public float speed;
    private Rigidbody rb;
    public AudioSource sound1;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        speed = 10;
        cnt1 = 0;

        cntText1.text = "Count: " + cnt1.ToString();
    }


    void FixedUpdate()
    {
        //cnt1++;
        //cntText1.text = cnt1.ToString();
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

    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("Pick Up"))
        {
            cnt1++;
            cntText1.text = "Count: " + cnt1.ToString();

            sound1.Play();
            other.gameObject.SetActive(false);
            //Destroy(other.gameObject);
        }
    }

}
