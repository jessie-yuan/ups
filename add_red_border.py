import cv2
import imageio

input_path = "video_incapable.mp4"
output_path = "video_incapable_bordered.mp4"
border_frames = range(119, 136)  # frames 119-135 inclusive
border_thickness = 40
border_color = (0, 0, 255)  # BGR red

cap = cv2.VideoCapture(input_path)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"Video: {width}x{height} @ {fps} fps, {total} frames")

video_writer = imageio.get_writer(output_path, fps=fps)

frame_idx = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if frame_idx in border_frames:
        t = border_thickness
        frame[:t, :] = border_color        # top
        frame[-t:, :] = border_color       # bottom
        frame[:, :t] = border_color        # left
        frame[:, -t:] = border_color       # right
        print(f"  Bordered frame {frame_idx}")
    # convert from bgr to rgb for imageio
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video_writer.append_data(frame)
    frame_idx += 1

cap.release()
video_writer.close()
print(f"Done. Wrote {frame_idx} frames to {output_path}")
