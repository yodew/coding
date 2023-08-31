#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-11-07 14:41 
"""
data = {
    "followup_id": "adfb48f45c2d11ed800d0242ac130003",
    "user_id": "f4a712c2bae511ec907e0242ac14000b",
    "detects": [
        "16bb4f5c5c0f11ed815a0242ac130011",
        "d6d1493c5c0e11edaf0a0242ac130011"
    ],
    "stores": [
        "162c50545c0f11ed815a0242ac130011",
        "d63419fa5c0e11edaf0a0242ac130011"
    ],
    "study_days": [
        0,
        343
    ],
    "groups": [
        "ae2e1d6a5c2d11ed800d0242ac130003"
    ],
    "status": "succeed",
    "created": 1667558678,
    "updated": 1667558679
}


def main():
    detects = data["detects"]
    stores = data["stores"]
    new_data = []
    for i in range(len(detects)):
        new_data.append({
            "store_id": stores[i],
            "detect_id": detects[i]
        })
    # new_data = [{"detect_id": d, "store_id": s} for d in detects for s in stores]
    print(new_data)
    return new_data


def aa(dirname):
    data = []
    file_list = os.listdir(dirname)
    count = len(file_list)
    filename = os.path.join(dirname, file_list[0])
    tag = pydicom.read_file(filename)
    slice_thickness = float(tag.get("SliceThickness", -100))
    for filename in file_list:
        filepath = os.path.join(dirname, filename)
        tag = pydicom.read_file(filepath)
        instance_number = int(tag.get("InstanceNumber", 1))
        slice_location = tag.get("SliceLocation")
        data.append((instance_number, slice_location))
    data.sort(key=lambda x: x[0])

    sub_dirname = os.path.dirname(dirname)
    if get_system_service_name() == "SurgiPro":
        first_frame_slice_location = data[0][1]
        second_frame_slice_location = data[1][1]
        if first_frame_slice_location is not None and second_frame_slice_location is not None:
            slice_spacing = round(abs(float(second_frame_slice_location) - float(first_frame_slice_location)), 2)
            slice_spacing_limit = float(get_slice_spacing_limit())
            if slice_spacing > slice_spacing_limit:
                if del_sub_dir:
                    shutil.rmtree(sub_dirname)
                raise DICOMSeriesInstanceNumberLess(
                    "Dicom image slice_spacing: %s mm, slice_spacing_limit: %s mm.", "层间距不满足要求")
            # elif slice_spacing > slice_thickness:
            #     shutil.rmtree(sub_dirname)
            #     raise DICOMSeriesUnmatchedSliceSpacing(
            #         "Dicom image slice_thickness: %s mm, slice_spacing: %s mm." % (slice_thickness, slice_spacing),
            #         u"%s" % (UPLOAD_ERROR_MESSAGE["slice_spacing"][1] % (slice_thickness, slice_spacing)))

    min_instance_number = data[0][0]
    max_instance_number = data[-1][0]
    dcm_amount = max_instance_number - min_instance_number + 1
    if dcm_amount == count:
        return True
    if del_sub_dir:
        shutil.rmtree(sub_dirname)
    if dcm_amount > count:
        raise DICOMSeriesInstanceNumberMissing(
            "The image is missing %s frames." % (dcm_amount - count),
            u"%s" % (UPLOAD_ERROR_MESSAGE["frame_count"][0] % (dcm_amount - count)))
    elif dcm_amount < count:
        raise DICOMSeriesInstanceNumberRepeat(
            "There are duplicate frames in the image.",
            u"%s" % UPLOAD_ERROR_MESSAGE["frame_count"][1])



if __name__ == "__main__":
    main()
