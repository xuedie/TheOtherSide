﻿using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShowcaseTouchPointController : MonoBehaviour
{
    #region Singleton
    public static ShowcaseTouchPointController Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] ShowcaseTouchPoint[] touchPoints;
    [SerializeField] string resultText = "{0} people selected this option";
    public float loadingTime = 1.5f;
    public float waterIncreaseTime = 1f;
    public float resultTextFadeTime = 1f;
    public float resultTextDisplayTime = 4f;

    private void Start()
    {
        touchPoints = GetComponentsInChildren<ShowcaseTouchPoint>();
        LoadOptionText();
        SetWater();
        InitializePhidgetsInputCallback();
    }
    private void SetWater()
    {
        for (int i = 0; i < touchPoints.Length; ++i)
        {
            touchPoints[i].InitializeWater();
            int count = ResultLoader.Instance.GetRawOptionCount(touchPoints[i].id);
            touchPoints[i].SetWater(count);
        }
    }

    public void LoadOptionText()
    {
        for (int i = 0; i < touchPoints.Length; ++i)
        {
            string optionText = ShowcaseTemplateJsonLoader.Instance.GetOption(touchPoints[i].id);
            touchPoints[i].SetText(optionText);
        }
    }

    public void ShowResultText(int idx) {
        string optionResultText = String.Format(
            resultText,
            ResultLoader.Instance.GetOptionCount(touchPoints[idx].id));
        touchPoints[idx].SetResultText(optionResultText);
    }

    public void IncreaseWater(int idx) {
        touchPoints[idx].IncreaseWater(ResultLoader.Instance.GetRawOptionCount(touchPoints[idx].id));
    }

    public void ResetAllProgress()
    {
        foreach (ShowcaseTouchPoint tp in touchPoints)
        {
            tp.ResetProgress();
        }
    }

    public void EnableAll()
    {
        foreach (ShowcaseTouchPoint tp in touchPoints)
        {
            tp.interactionEnabled = true;
        }
    }

    public void DisableAll()
    {
        foreach (ShowcaseTouchPoint tp in touchPoints)
        {
            tp.interactionEnabled = false;
        }
    }

    public void DisableExcept(int idx)
    {
        for (int i = 0; i < touchPoints.Length; ++i)
        {
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

    public void EnableArrowEffect()
    {
        foreach (ShowcaseTouchPoint tp in touchPoints)
        {
            tp.SetArrowEffect(true);
        }
    }

    public void DisableArrowEffect()
    {
        foreach (ShowcaseTouchPoint tp in touchPoints)
        {
            tp.SetArrowEffect(false);
        }
    }

    public void PlayDropAnimation(int idx) {
        touchPoints[idx].PlayDropAnimation();
    }

    public void OnEndDroppingAnimation() {
        ShowcaseTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Display);
    }


    public void OnStartTouch(int id)
    {
        // touch starts on touch point
        // change state
        ShowcaseTemplateController.Instance.SetActiveOption(id);
        ShowcaseTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Loading);
    }

    public void OnAbortTouch(int id)
    {
        // playtest logging
        PlaytestController.Instance.LogFailAttempt();
        // touch aborted on touch point, back to idle 
        // change state
        ShowcaseTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Idle);
        ShowcaseTemplateController.Instance.SetActiveOption(-1);
    }

    public void OnEndTouch(int id)
    {
        // playtest logging
        PlaytestController.Instance.LogEndTime();
        // touch finished on touch point, scroll main bubble with answer
        // change state
        ShowcaseTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Reacting);
    }

    // Phidgets sensor input
    void InitializePhidgetsInputCallback() {
        if (PhidgetsInputManager.Instance) {
            PhidgetsInputManager.Instance.OnIncreseProgressCallback =
                new PhidgetsInputManager.OnIncreaseProgress(IncreaseTouchpointProgrss);
            PhidgetsInputManager.Instance.OnStopProgressCallback =
                new PhidgetsInputManager.OnStopProgress(StopTouchpointProgrss);

        }
    }

    public void IncreaseTouchpointProgrss(int idx) {
        touchPoints[idx].IncreaseProgress(Time.deltaTime / loadingTime);
    }

    public void StopTouchpointProgrss(int idx)
    {
        touchPoints[idx].StopProgress();
    }
}

