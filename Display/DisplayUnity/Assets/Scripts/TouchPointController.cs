﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TouchPointController : MonoBehaviour
{
    #region Singleton
    public static TouchPointController Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] TouchPoint[] touchPoints;
    public float loadingTime = 1.5f;

    private void Start()
    {
        touchPoints = GetComponentsInChildren<TouchPoint>();
        LoadOptionText();
    }

    public void LoadOptionText() {
        for(int i = 0; i < touchPoints.Length; ++i) {
            string optionText = JsonLoader.Instance.GetOption(touchPoints[i].id);
            touchPoints[i].SetText(optionText);
            touchPoints[i].AdjustContainer();
        }
    }

    public void ResetAllProgress() {
        foreach (TouchPoint tp in touchPoints)
        {
            tp.ResetProgress();
        }
    }

    public void EnableAll() {
        foreach (TouchPoint tp in touchPoints)
        {
            tp.interactionEnabled = true;
        }
    }

    public void DisableAll() {
        foreach (TouchPoint tp in touchPoints)
        {
            tp.interactionEnabled = false;
        }
    }

    public void DisableExcept(int idx) {
        for (int i = 0; i < touchPoints.Length; ++i) {
            if (i == idx)
            {
                touchPoints[i].interactionEnabled = true;
            }
            else
            {
                touchPoints[i].interactionEnabled = false;
            }
        }
    }

    public void OnStartTouch(int id) {
        // touch starts on touch point
        // change state
        TextTemplateController.Instance.SetActiveOption(id);
        TextTemplateController.Instance.SetTemplateState(TextTemplateController.TemplateState.Loading);
    }

    public void OnAbortTouch(int id) {
        // playtest logging
        PlaytestController.Instance.LogFailAttempt();
        // touch aborted on touch point, back to idle 
        // change state
        TextTemplateController.Instance.SetTemplateState(TextTemplateController.TemplateState.Idle);
        TextTemplateController.Instance.SetActiveOption(-1);
    }

    public void OnEndTouch(int id)
    {
        // playtest logging
        PlaytestController.Instance.LogEndTime();
        // touch finished on touch point, scroll main bubble with answer
        // change state
        TextTemplateController.Instance.SetTemplateState(TextTemplateController.TemplateState.Reacting);
    }
}
