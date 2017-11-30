using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Player1 : MonoBehaviour {

	int cnt1;
	public Text countText;
	// Use this for initialization
	void Start () {
		cnt1 = 0;
	}
	
	// Update is called once per frame
	void Update () {
		cnt1++;
		countText.text = "Count:" + cnt1.ToString ();
	}
}
